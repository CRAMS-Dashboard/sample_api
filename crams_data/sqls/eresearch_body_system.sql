INSERT INTO crams_fundingbody (`name`, email) VALUES ('CRAMS', 'crams@crams.com');
INSERT INTO crams_fundingscheme (funding_scheme, funding_body_id) VALUES ('CRAMS-FS', (SELECT id from crams_fundingbody where `name` = 'CRAMS'));
INSERT INTO crams_eresearchbody (`name`, email) VALUES ('CRAMS-ERB', 'crams@crams.com');
INSERT INTO crams_eresearchbodysystem (e_research_body_id, `name`) VALUES ((SELECT id from crams_eresearchbody where `name` = 'CRAMS-ERB'), 'CRAMS-ERB-SYS');
INSERT INTO crams_eresearchbodyidkey (`key`, e_research_body_id, `type`) VALUES ('CRAMS',(SELECT id from crams_eresearchbody where `name` = 'CRAMS-ERB'), 'I');
INSERT INTO crams_provider (id, `name`, active,  created_by_id, creation_ts, description, last_modified_ts, start_date, updated_by_id) VALUES (1, 'CRAMS', true, NULL, '2021-02-25 16:33:18.000000', NULL, '2021-02-25 16:33:18.000000', '2021-02-25', NULL);