# sqlalchemy-challenge

This assigment required me to display skills utllizing SQLAlchemy and Python to do basic climate analysis and data exploration of your climate db. 


THE CODES WRITTEN FOR THE ASSIGNMENT ARE IN /instructions:

    The climate_starter.ipynb contains the SQLAlchemy. 
        - imported modules: matplotlib, numpy, pandas, datetime,
            sqlalchemy.orm
        
        -SQLite DB name: measurement, station
    
        - Bonus Challenge Assignment completed.
            codes were partially provided in the notebooks. 

    

    app.py contains the Step 2 for the Climate App. Which was used to design a Flask API based on the queries.
        -Flask was used to create the routes. 
        -Routes: 
            - "/" = home 
            - "/api/v1.0/precipitation" = precipitation
            - "/api/v1.0/stations" = station
            - "/api/v1.0/tobs" = temperatures
            -"/api/v1.0/<start>"
            -"/api/v1.0/<start>/<end>" = tmin,tavg,tmax
    
    