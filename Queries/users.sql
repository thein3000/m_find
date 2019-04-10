-- SQLite
select username, first_name, email,* from auth_user;
select profile_id, mobile, twitter, facebook, email ,instrument_id, genre_id, is_musician, description from musi_find_backend_profile;
--SELECT * FROM musi_find_backend_instrument;
--SELECT * FROM musi_find_backend_genre;
--SELECT * FROM musi_find_backend_publication;
--SELECT * FROM musi_find_backend_rating;
sELECT * FROM musi_find_backend_follow;
--Raul
UPDATE musi_find_backend_profile SET is_musician = True where profile_id =2;
UPDATE musi_find_backend_profile SET facebook = 'raul.emg' where profile_id =2;
UPDATE musi_find_backend_profile SET mobile = '8125828661' where profile_id =2;
--Oscar
UPDATE musi_find_backend_profile SET twitter = 'OscarAbregoDiaz' where profile_id =1;
UPDATE musi_find_backend_profile SET mobile = '8113995183' where profile_id =1;
UPDATE musi_find_backend_profile SET facebook = 'oabrego2' where profile_id =1;
--Hugo
UPDATE musi_find_backend_profile SET is_musician = True where profile_id =9;

--DELETE FROM musi_find_backend_profile WHERE profile_id = 10 OR profile_id = 12
--DELETE FROM auth_user WHERE id = 10 OR id=11 OR id = 12