import React from 'react';
import NavBar from "../../components/NavBar.js";
import axios from 'axios';
import { useState } from 'react';
import { makeStyles } from "@material-ui/core/styles";
import project1 from "../../files/images/html-css-javascript-lg.jpg"
import {
    Box,
    Typography,
    Text,
    Button,
    Grid,
    Image,
    Card,
    CardMedia,
    Divider
} from "@material-ui/core";

const useStyles = makeStyles({
  backColor: {
    background: "#AD5F3D",
    height: "100%",
    margin: "-4rem 0 0rem"
  },  
  heading: {
      position: "relative",
      color: "white",
      margin: "0 0 3rem"
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
      background: "grey",
      size: "small",
      float: "right"
    },
    imageCard: {
      height: "20rem",
      width: "14rem"
    },
    info: {
      marginTop: "3rem",
      justifyContent: "center",
      alignItems: "center",
      marginRight: "2rem",
    },
    image: {
      width: "100%",
      height: "100%"
    },
    imagePlacement: {
      marginLeft: "7rem"
    }
})

const filmInfo = [
    {
        filmName: "1917",
        filmReleaseDate: "2018",
        filmGenre: "Drama, War",
        filmLength: "1h59min",
        filmDirector: "Sam Mendes",
        filmPlot: "April 6th, 1917. As a regiment assembles to wage war deep in enemy territory, two soldiers are assigned to race against time and deliver a message that will stop 1,600 men from walking straight into a deadly trap.",
        filmTrailer: "trailer link",
        filmImage: project1
    }
]

const periodInfo = [
    {
        periodName: "Modern History",
        subperiodName: "World War I",
        periodSummary: "World War I began in 1914 after the assassination of Archduke Franz Ferdinand and lasted until 1918. During the conflict, Germany, Austria-Hungary, Bulgaria and the Ottoman Empire (the Central Powers) fought against Great Britain, France, Russia, Italy, Romania, Japan and the United States (the Allied Powers).",
        periodImage: "link"
    }
]

export default function SelectedFilm() {

    const [filmList, setFilmList] = useState([]);

    const response = axios.get("http://127.0.0.1:5000/selected_film").then((films) => setFilmList(films.data))
    // to get an item: {filmList}

    const classes = useStyles()
                  // <Image component="img" alt="Film1" source={lsItem.filmImage} className={classes.imageBox}>

  return (
    <>
      <NavBar/>
      <Box component= "div" className={classes.backColor}>
        
        <>
          <Button variant="contained" href="/films_list" className = {classes.button}>
            Back to Films List
          </Button>
        </>

        <Box component="div" className={classes.mainContainer}>

          {filmInfo.map((lsItem) => (
            <>
              <Grid container spacing={2}>
                <Grid xs={6}>
                  <Typography variant="h3" className={classes.heading}>
                    {lsItem.filmName} 
                  </Typography>
                  <div className={classes.info}>
                    <Typography variant="h6">
                      Release date: {lsItem.filmReleaseDate} 
                    </Typography>
                    <Typography variant="h6">
                      Genre: {lsItem.filmGenre}
                    </Typography>
                    <Typography variant="h6">
                      Film Length: {lsItem.filmLength}
                    </Typography>
                    <Typography variant="h6">
                      Director: {lsItem.filmDirector}
                    </Typography>
                  </div>
                </Grid>
                <Grid xs={6} >
                  <Card className ={classes.imageCard} >
                    <CardMedia component="img" alt="Film1" image={lsItem.filmImage} className ={classes.image}/>
                  </Card>
                </Grid>
                <Grid xs={12}>
                  <>
                    <Typography variant="h6">
                      Plot:
                    </Typography>
                    <Typography variant="h6">
                      {lsItem.filmPlot}
                    </Typography>
                    <Typography variant="h6">
                      Movie Trailer: {lsItem.filmTrailer}
                    </Typography>
                  </>
                </Grid>
              </Grid>
            </>
          ))}  

          <hr />

          {periodInfo.map((lsItem) => (
            <>
              <Grid xs={12}>
                <div className={classes.info}>
                  <Typography variant="h6">
                    Historic Period: {lsItem.periodName}
                  </Typography>
                  <Typography variant="h6">
                    Historic Subperiod: {lsItem.subperiodName}
                  </Typography>
                </div>
              </Grid>

              <Grid xs={12}>
                <div className={classes.info}>
                  <Typography variant="h6">
                    Subperiod Summary:
                  </Typography>
                  <Typography variant="h6">
                    {lsItem.periodSummary}
                  </Typography>
                </div>
              </Grid>
            </>
          ))}
        </Box>
      </Box>
    </>
  );
}
