
--Raul
UPDATE musi_find_backend_profile SET is_musician = True where profile_id =2;
UPDATE musi_find_backend_profile SET facebook = 'raul.emg' where profile_id =2;
--Oscar
UPDATE musi_find_backend_profile SET twitter = 'OscarAbregoDiaz' where profile_id =1;
UPDATE musi_find_backend_profile SET facebook = 'oabrego2' where profile_id =1;
--Hugo
UPDATE musi_find_backend_profile SET is_musician = True where profile_id =9;
-- All users
UPDATE auth_user SET email = 'oscar.abrego1998@gmail.com' where id = 1;
UPDATE auth_user SET email = 'raul.emg@gmail.com' where id = 2;
UPDATE auth_user SET email = 'samantha.nieto@gmail.com' where id = 3;
UPDATE auth_user SET email = 'jaime.prueba@gmail.com' where id = 4;
UPDATE auth_user SET email = 'pedro.prueba@gmail.com' where id = 5;
UPDATE auth_user SET email = 'juan.prueba@gmail.com' where id = 6;
UPDATE auth_user SET email = 'rodrigo.prueba@gmail.com' where id = 7;
UPDATE auth_user SET email = 'martinez.prueba@gmail.com' where id = 8;
UPDATE auth_user SET email = 'hugo.prueba@gmail.com' where id = 9;
UPDATE auth_user SET email = 'luis.prueba@gmail.com' where id = 10;
-- All profiles
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 1;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 2;
-- UPDATE musi_find_backend_profile SET gender = 'Femenina' where profile_id = 3;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 4;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 5;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 6;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 7;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 8;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 9;
-- UPDATE musi_find_backend_profile SET gender = 'Masculino' where profile_id = 10;

--DELETE FROM musi_find_backend_profile WHERE profile_id = 10 OR profile_id = 12
--DELETE FROM auth_user WHERE id = 10 OR id=11 OR id = 12


-- SQLite
select id,username, first_name, email,* from auth_user;
--select profile_id, mobile, twitter, facebook, email ,instrument_id, genre_id, is_musician, description from musi_find_backend_profile;
--SELECT * FROM musi_find_backend_instrument;
--SELECT * FROM musi_find_backend_genre;
--SELECT * FROM musi_find_backend_publication;
--SELECT * FROM musi_find_backend_rating;
--sELECT * FROM musi_find_backend_follow;
--SELECT * FROM musi_find_backend_message;
--SELECT * FROM musi_find_backend_ban;