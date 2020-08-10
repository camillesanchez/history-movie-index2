import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import Truncate from 'react-truncate';
import {
    Box,
    Grid,
    Card,
    CardActionArea,
    CardActions,
    CardContent,
    CardMedia,
    Typography
} from "@material-ui/core"
import NavBar from "../../components/NavBar.js";
import project1 from "../../files/images/html-css-javascript-lg.jpg"
import project2 from "../../files/images/javascript-fullstack.jpg"
import project3 from "../../files/images/react-redux.jpg"
import project4 from "../../files/images/mern-stack.jpg"
import axios from 'axios';
import { useState } from 'react';

const useStyles = makeStyles({
    mainContainer: {
        background: "#AD5F3D",
        height: "100%"
    },
    cardContainer: {
        maxWidth:300,
        margin: "1rem auto"
    },
    card: {
        height: "22rem"
    },
    heading: {
        color: "#FFB5A1",
        padding: "3rem 0 1.4rem",
        textTransform: "uppercase"
    }
})

const selectedFilmsList = [
    {
        filmName: "1917",
        filmPlot: "About film",
        filmImage: project1,
        filmPath: "/selected_film"
    },
    {
        filmName: "They shall not grow old",
        filmPlot: "About filmedn;wj enkjebdfkdjbfkbebkebk ejbkbekbdkebdkeb jdkbjekbdjkejbdkejbdkjbkebjdke bjdkejbdkejbdkejbdkbjekjbdkbkebdjjedbkebdkebdkejbdejk",
        filmImage: project2,
        filmPath: "/selected_film"
    },
    {
        filmName: "Journey's end",
        filmPlot: "About film",
        filmImage: project3,
        filmPath: "/selected_film"
    },
    {
        filmName: "Light between oceans",
        filmPlot: "About film",
        filmImage: project4,
        filmPath: "/selected_film"
    },
    {
        filmName: "Titanic",
        filmPlot: "About film",
        filmImage: "link",
        filmPath: "/selected_film"
    },
    {
        filmName: "War Horse",
        filmPlot: "About film",
        filmImage: "link",
        filmPath: "/selected_film"
    },
    {
        filmName: "Tolkien",
        filmPlot: "About film",
        filmImage: "link",
        filmPath: "/selected_film"
    }
]

const FilmsList = () => {
    
    const [filmList, setFilmList] = useState([]);

    const response = axios.get("http://127.0.0.1:5000/films_list").then((films) => setFilmList(films.data))
    // to get an item: {filmList}
    
    const classes = useStyles()

    return (
        <>
            <NavBar/>

            <Box component= "div" className={classes.mainContainer}>
                <div className= {classes.heading}>
                    <Typography variant="h4" align="center" >
                        Films for:
                    </Typography>
                    <Typography variant="h4" align="center">
                        Modern History - World War I
                    </Typography>
                </div>
                <Grid container justify="center">
                    
                    {selectedFilmsList.map((lsItem) => (
                        <Grid item xs={12} sm={8} md={6} className={classes.cardContainer} >
                            <Card className= {classes.card}>
                                <CardActionArea href={lsItem.filmPath} >
                                    <CardMedia 
                                        component="img" 
                                        alt="Film1" 
                                        height="140" 
                                        image={lsItem.filmImage}
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5">
                                            Film Title: {lsItem.filmName}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            <Truncate lines={4} ellipsis={"..."}>
                                                Description: {lsItem.filmPlot}
                                            </Truncate>
                                        </Typography>
                                    </CardContent>
                                </CardActionArea>
                            </Card>

                        </Grid>
                    ))}
                    
                </Grid>
            </Box>
        </>
        )
}

export default FilmsList;

