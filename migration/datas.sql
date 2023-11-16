-- Table: public.datas

-- DROP TABLE IF EXISTS public.datas;

-- SEQUENCE: public.datas_aut_inc

-- DROP SEQUENCE IF EXISTS public.datas_aut_inc;

CREATE TABLE IF NOT EXISTS public.datas
(
    id bigint NOT NULL DEFAULT nextval('datas_aut_inc'::regclass),
    type character varying(50) COLLATE pg_catalog."default",
    froms character varying(25) COLLATE pg_catalog."default",
    status character varying(50) COLLATE pg_catalog."default",
    text text COLLATE pg_catalog."default",
    attachment character varying(255) COLLATE pg_catalog."default",
    meta text COLLATE pg_catalog."default",
    data_date character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT datas_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.datas
    OWNER to postgres;

CREATE SEQUENCE IF NOT EXISTS public.datas_aut_inc
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    OWNED BY datas.id;

ALTER SEQUENCE public.datas_aut_inc
    OWNER TO postgres;