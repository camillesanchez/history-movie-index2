# The History Movie Index

## Overall Project:

This web app was built to help teachers, students and parents alike to find movies set in a specific time period. On this app, each movie is classed according to the time period it's set in.

## Goal:

The 21st century is a Digital Era. So, books should not be the only resource to learn information. 

I believe maintsream media can help young generations (and older) visualize time periods far out of reach. Thus, helping them memorize key characters and events from our History. 

## Usage:

1. To use this platform, you must first download the "title.basics.tsv" dataset from ([IMDb - interfaces](https://www.imdb.com/interfaces/)). 

2. Upload it in Website\ Code/flask_backend_database directory.

3. To get your database loaded up. Run the following 3 scripts in this order:

        python imdb_create_db.py
        python imdb_import_periods_subperiods_keywords.py
        python imdb_import_films.py
        python imdb_import_make_connections.py

4. To launch the Flask / React app, run the following prompts:
        
-  in the flask_backend directory, launch flask:

        export FLASK_APP=app.py
        flask run

- in the react_frontend directory, launch react:

        yarn start or npm start

## License

[MIT License](https://github.com/camillesanchez/history-movie-index2/blob/master/LICENSE)

## Contributing

For any changes, please open an issue first to discuss what you would like to change. 