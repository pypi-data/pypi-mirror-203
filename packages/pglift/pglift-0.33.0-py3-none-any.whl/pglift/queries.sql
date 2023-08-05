-- name: role_exists
SELECT true FROM pg_roles WHERE rolname = %(username)s;

-- name: role_create
CREATE ROLE {username} {options};

-- name: role_alter
ALTER ROLE {username} {options};

-- name: role_inspect
SELECT
    r.rolname AS name,
    r.rolpassword IS NOT NULL AS has_password,
    r.rolinherit AS inherit,
    r.rolcanlogin AS login,
    r.rolsuper AS superuser,
    r.rolcreatedb AS createdb,
    r.rolcreaterole AS createrole,
    r.rolreplication AS replication,
    CASE WHEN r.rolconnlimit <> - 1 THEN
        r.rolconnlimit
    ELSE
        NULL
    END AS connection_limit,
    r.rolvaliduntil AS validity,
    ARRAY(SELECT a.rolname
          FROM pg_catalog.pg_auth_members m
          JOIN pg_catalog.pg_authid a ON (m.roleid = a.oid)
          WHERE m.member = r.oid) as in_roles
FROM
    pg_authid r
WHERE
    r.rolname = %(username)s;

-- name: role_grant
GRANT {rolname} TO {rolspec};

-- name: role_revoke
REVOKE {rolname} FROM {rolspec};

-- name: role_list_names
SELECT rolname from pg_roles ORDER BY rolname;

-- name: role_list
SELECT
    r.rolname as name,
    r.rolpassword IS NOT NULL AS has_password,
    r.rolinherit AS inherit,
    r.rolcanlogin AS login,
    r.rolsuper AS superuser,
    r.rolcreatedb AS createdb,
    r.rolcreaterole AS createrole,
    r.rolreplication AS replication,
    CASE WHEN r.rolconnlimit <> - 1 THEN
        r.rolconnlimit
    ELSE
        NULL
    END AS connection_limit,
    r.rolvaliduntil AS validity,
    ARRAY(SELECT a.rolname
          FROM pg_catalog.pg_auth_members m
          JOIN pg_catalog.pg_authid a ON (m.roleid = a.oid)
          WHERE m.member = r.oid) as in_roles
FROM
    pg_catalog.pg_authid r
WHERE
    r.rolname !~ '^pg_'
ORDER BY 1;

-- name: role_drop
DROP ROLE {username};

-- name: role_drop_owned
DROP OWNED BY {username};

-- name: role_drop_reassign
REASSIGN OWNED BY {oldowner} TO {newowner};

-- name: database_exists
SELECT true FROM pg_database WHERE datname = %(database)s;

-- name: database_create
CREATE DATABASE {database} {options};

-- name: database_alter
ALTER DATABASE {database} {options};

-- name: database_encoding
SELECT
    pg_encoding_to_char(encoding) AS encoding
FROM pg_database WHERE datname = current_database();

-- name: database_inspect
SELECT
    db.datname as name,
    r.rolname AS owner,
    (
        SELECT s.setconfig FROM pg_db_role_setting s
        WHERE s.setdatabase = db.oid AND s.setrole = 0
    ) AS settings
FROM
    pg_database db
    JOIN pg_authid r ON db.datdba = r.oid
WHERE
    db.datname = current_database();

-- name: database_list
SELECT d.datname as "name",
    pg_catalog.pg_get_userbyid(d.datdba) as "owner",
    pg_catalog.pg_encoding_to_char(d.encoding) as "encoding",
    d.datcollate as "collation",
    d.datctype as "ctype",
    coalesce(d.datacl, '{{}}'::aclitem[]) AS "acls",
    pg_catalog.pg_database_size(d.datname) as "size",
    t.spcname as "tablespace",
    pg_catalog.pg_tablespace_location(t.oid) as "tablespace_location",
    pg_catalog.pg_tablespace_size(t.oid) as "tablespace_size",
    pg_catalog.shobj_description(d.oid, 'pg_database') as "description"
FROM pg_catalog.pg_database d
JOIN pg_catalog.pg_tablespace t on d.dattablespace = t.oid
WHERE datallowconn {where_clause}
ORDER BY 1;

-- name: database_drop
DROP DATABASE {database} {options};

-- name: database_default_acl
WITH default_acls AS (
    SELECT
        pg_namespace.nspname AS schema,
        pg_default_acl.defaclobjtype AS objtype,
        aclexplode(pg_default_acl.defaclacl) AS acl
    FROM
        pg_default_acl
        JOIN pg_namespace ON pg_namespace.oid = pg_default_acl.defaclnamespace
)
SELECT
    current_database() AS database,
    default_acls.schema,
    pg_roles.rolname AS role,
    CASE default_acls.objtype
    WHEN 'f' THEN
        'FUNCTION'
    WHEN 'r' THEN
        'TABLE'
    WHEN 'S' THEN
        'SEQUENCE'
    WHEN 'T' THEN
        'TYPE'
    WHEN 'n' THEN
        'SCHEMA'
    ELSE
        'UNKNOWN'
    END AS object_type,
    array_agg(DISTINCT (default_acls.acl).privilege_type) AS privileges
FROM
    default_acls
    JOIN pg_roles ON ((acl).grantee = pg_roles.oid)
{where_clause}
GROUP BY
    schema,
    role,
    object_type
ORDER BY
    schema,
    role,
    object_type;

-- name: database_privileges
WITH relacl AS (
    SELECT
        c.oid,
        rolname,
        array_agg(relacl.privilege_type) AS relacl
    FROM
        pg_catalog.pg_class c
        CROSS JOIN aclexplode(c.relacl) as relacl
        JOIN pg_roles ON (relacl.grantee = pg_roles.oid)
        LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
    GROUP BY 1, 2
),
attacl AS (
    SELECT
        c.oid,
        attname,
        rolname,
        array_agg(attacl.privilege_type) AS attacl
    FROM
        pg_catalog.pg_class c
        JOIN pg_catalog.pg_attribute ON attrelid = c.oid
        CROSS JOIN aclexplode(pg_catalog.pg_attribute.attacl) as attacl
        JOIN pg_roles ON (attacl.grantee = pg_roles.oid)
    WHERE
        NOT attisdropped
        AND attacl IS NOT NULL
    GROUP BY 1, 2, 3
),
attacl_agg AS (
    SELECT
        oid,
        attacl.rolname,
        json_object_agg(
            attacl.attname,
            attacl.attacl
        ) as attacl
    FROM attacl
    GROUP BY 1, 2
)
SELECT
    current_database() AS database,
    n.nspname AS schema,
    c.relname AS object_name,
    CASE c.relkind
        WHEN 'r' THEN
            'TABLE'
        WHEN 'v' THEN
            'VIEW'
        WHEN 'm' THEN
            'MATERIALIZED VIEW'
        WHEN 'S' THEN
            'SEQUENCE'
        WHEN 'f' THEN
            'FOREIGN TABLE'
        WHEN 'p' THEN
            'PARTITIONED TABLE'
        ELSE
            'UNKNOWN'
        END
    AS object_type,
    pg_roles.rolname AS role,
    coalesce(a.relacl, '{{}}'::text[]) AS privileges,
    coalesce(b.attacl, '{{}}'::json) AS column_privileges
FROM pg_class c
CROSS JOIN pg_roles
LEFT JOIN relacl a ON c.oid = a.oid AND pg_roles.rolname = a.rolname
LEFT JOIN attacl_agg b ON c.oid = b.oid AND pg_roles.rolname = b.rolname
LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE
    c.relkind IN ('r', 'v', 'm', 'S', 'f', 'p')
    AND n.nspname !~ '^pg_'
    AND pg_table_is_visible(c.oid)
    AND (a.relacl IS NOT NULL OR attacl IS NOT NULL)
    {where_clause};

-- name: list_schemas
SELECT n.nspname AS name
FROM pg_catalog.pg_namespace n
WHERE n.nspname !~ '^pg_' AND n.nspname <> 'information_schema'
ORDER BY 1;

-- name: create_schema
CREATE SCHEMA {schema};

-- name: drop_schema
DROP SCHEMA {schema} CASCADE;

-- name: list_extensions
SELECT
    extname AS name,
    s.nspname AS schema,
    extversion AS version
FROM pg_extension
LEFT JOIN pg_namespace s ON s.oid = pg_extension.extnamespace
WHERE extname != 'plpgsql' ORDER BY extname;

-- name: alter_extension
ALTER EXTENSION {extension} {opts};

-- name: drop_extension
DROP EXTENSION IF EXISTS {extension} CASCADE;

-- name: extension_default_version
SELECT default_version FROM pg_available_extensions WHERE name = %(extension_name)s;
