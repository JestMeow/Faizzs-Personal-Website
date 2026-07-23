CREATE TABLE public.projects_metadata (
	id int4 GENERATED ALWAYS AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL,
	title varchar NULL,
	description varchar NULL,
	github_url varchar NULL,
	priority int4 DEFAULT 0 NOT NULL,
	CONSTRAINT projects_metadata_pkey PRIMARY KEY (id)
);

CREATE TABLE public.soundcloud_widget_metadata (
	id int4 GENERATED ALWAYS AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL,
	title varchar NULL,
	track varchar NULL,
	musescore_url varchar NULL,
	priority int4 DEFAULT 0 NOT NULL,
	CONSTRAINT soundcloud_preview_data_pkey PRIMARY KEY (id)
);

