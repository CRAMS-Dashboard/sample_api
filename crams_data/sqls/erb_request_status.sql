INSERT INTO crams_allocation_erbrequeststatus(display_name, e_research_system_id, request_status_id, extension_count_data_point) values('Extension Submitted', (SELECT id from crams_eresearchbodysystem where `name` = 'CRAMS-ERB-SYS'), (SELECT id from crams_allocation_requeststatus where code = 'X'), 1);
INSERT INTO crams_allocation_erbrequeststatus(display_name, e_research_system_id, request_status_id, extension_count_data_point) values('Extension Declined', (SELECT id from crams_eresearchbodysystem where `name` = 'CRAMS-ERB-SYS'), (SELECT id from crams_allocation_requeststatus where code = 'J'), 1);
INSERT INTO crams_allocation_erbrequeststatus(display_name, e_research_system_id, request_status_id, extension_count_data_point) values('Extension Approved', (SELECT id from crams_eresearchbodysystem where `name` = 'CRAMS-ERB-SYS'), (SELECT id from crams_allocation_requeststatus where code = 'A'), 1);
INSERT INTO crams_allocation_erbrequeststatus(display_name, e_research_system_id, request_status_id, extension_count_data_point) values('Extension Provisioned', (SELECT id from crams_eresearchbodysystem where `name` = 'CRAMS-ERB-SYS'), (SELECT id from crams_allocation_requeststatus where code = 'P'), 1);
