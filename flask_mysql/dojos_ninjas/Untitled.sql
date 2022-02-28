-- SELECT * FROM ninjas JOIN dojos ON dojo_id = dojos.id;
-- SELECT * FROM dojos;
SELECT * FROM ninjas LEFT JOIN dojos ON dojo_id = dojos.id WHERE dojos.id = 7;