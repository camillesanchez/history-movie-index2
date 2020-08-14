import React from 'react';
import NavBar from "../../components/NavBar.js";
import axios from 'axios';
import { useState, useEffect } from 'react';
import { makeStyles } from "@material-ui/core/styles";
import {
    Box,
    Typography,
    Button,
    Grid,
    Card,
    CardMedia
} from "@material-ui/core";
import { useParams } from "react-router";
import Rectangle from 'react-rectangle';

const useStyles = makeStyles({
  backColor: {
    background: "#AD5F3D",
    minHeight: "1080px",
    margin: "-4rem 0 0rem"
  },  
  heading: {
      position: "relative",
      color: "white",
      margin: "0 5rem 3rem 0"
    },
    mainContainer: {
        margin: "4rem",
        height: "100%"
    },
    button:{
      marginTop: "1rem",
      marginBottom: "1rem",
      marginRight: "3rem",
      color: "black",
      background: "#B5A093",
      size: "small",
      float: "right"
    },
    imageCard: {
      height: "20rem",
      width: "14rem",
      margin: "0 3rem 1rem 3rem"
    },
    info: {
      marginTop: "3rem",
      justifyContent: "center",
      alignItems: "center",
      marginRight: "2rem",
      color: "#black"
    },
    image: {
      width: "100%",
      height: "100%"
    },
    imagePlacement: {
      marginLeft: "7rem"
    },
    trailerHyperlink: {
      color: "black",
      textDecorationLine: "none"
    },
    plotContainer: {
      marginTop: "2rem"
    }
})

export default function SelectedFilm() {

    const [filmList, setFilmList] = useState([]);

    const { film_id, subperiod_id } = useParams();

    useEffect(() => {
        axios.get(`http://127.0.0.1:5000/selected_film/${subperiod_id}/${film_id}`).then((films) => setFilmList(films.data));
    },[]);

    const classes = useStyles()

  return (
    <>
      <NavBar/>
      <Box component= "div" className={classes.backColor}>
        
        <>
          <Button variant="contained" href={`/films_list/${subperiod_id}`} className = {classes.button}>
            Back to Films List
          </Button>
        </>

        <Box component="div" className={classes.mainContainer}>

            <>
              <Grid container spacing={2}>
                <Grid xs={6}>
                  <Typography variant="h3" className={classes.heading}>
                    {filmList["film_title"]} 
                  </Typography>
                  <div className={classes.info}>
                    <Typography variant="h6">
                      <b>Release date:</b> {filmList["film_release_date"]} 
                    </Typography>
                    {filmList["film_genres"] !== "Unknown" && (
                      <>
                        <Typography variant="h6">
                          <b>Genre:</b> {filmList["film_genres"]}
                        </Typography>
                      </>
                    )}

                    <Typography variant="h6">
                      <b>Film Length:</b> {filmList["film_runtime"]}
                    </Typography>
                    <Typography variant="h6">
                      <b>Director:</b> {filmList["film_directors"]}
                    </Typography>
                    {filmList["film_writers"] !== "Unknown" && (
                      <>
                        <Typography variant="h6">
                          <b>Writer:</b> {filmList["film_writers"]}
                        </Typography>
                      </>
                    )}
                  </div>
                </Grid>
                <Grid xs={6} >
                  <Card className ={classes.imageCard} >
                    <CardMedia component="img" alt={filmList["film_title"]} image={filmList["film_image_url"]} className ={classes.image}/>
                  </Card>
                </Grid>
                <Grid xs={12} className={classes.plotContainer}>
                  <>
                    <Typography variant="h6" >
                      <b>Plot:</b>
                    </Typography>
                    <Typography variant="h6">
                      {filmList["film_plot"]}
                    </Typography>
                      {filmList["trailer_url"]  && (
                        <>
                          <Typography variant="h7">
                            <a href= {filmList["trailer_url"]} className={classes.trailerHyperlink}>
                              Film Trailer Link
                            </a>
                          </Typography>
                        </>
                      )}
                  </>
                </Grid>
              </Grid>
            </>
            <Rectangle aspectRatio={[7,0.02]}>
              <div style={{margin: "2rem 0 2rem -0.4rem", background: "#B5A093", width: "30%", height: "100%"}} />
            </Rectangle>

            <>
              <Grid xs={12}>
                <div className={classes.info}>
                  <Typography variant="h6">
                    <b>Historic Period:</b> {filmList["film_period"]}
                  </Typography>
                  <Typography variant="h6">
                    <b>Historic Subperiod:</b> {filmList["film_subperiod"]}
                  </Typography>
                </div>
              </Grid>
            </>
        </Box>
      </Box>
    </>
  );
}
