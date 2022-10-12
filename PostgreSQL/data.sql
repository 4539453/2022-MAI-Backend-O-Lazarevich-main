INSERT INTO
  public.film (uuid, title, year)
VALUES
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d4e',
    'The Godfather',
    1972
  ),
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d4f',
    'The Godfather: Part II',
    1974
  ),
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d50',
    'The Dark Knight',
    2008
  );

INSERT INTO
  public.director (uuid, name)
VALUES
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d51',
    'Francis Ford Coppola'
  ),
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d52',
    'Christopher Nolan'
  );

INSERT INTO
  public.film_director (film_uuid, director_uuid)
VALUES
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d4e',
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d51'
  ),
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d4f',
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d51'
  ),
  (
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d50',
    'f4d4e7c3-3b9a-4f3b-9f6d-4b4a4c7c4d52'
  );
