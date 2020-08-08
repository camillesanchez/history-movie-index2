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
    Button,
    Typography,
    Paper,
    List,
    Link 
} from "@material-ui/core"
import NavBar from "../../components/NavBar.js";
import project1 from "../../files/images/html-css-javascript-lg.jpg"
import project2 from "../../files/images/javascript-fullstack.jpg"
import project3 from "../../files/images/react-redux.jpg"
import project4 from "../../files/images/mern-stack.jpg"


const useStyles = makeStyles({
    mainContainer: {
        background: "#233",
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
        color: "tomato",
        padding: "3rem 0 0.4rem",
        textTransform: "uppercase"
    }
})

const filmList = [
    {
        filmName: "1917",
        filmPlot: "About film",
        filmImage: project1,
        filmPath: "/single_film_page"
    },
    {
        filmName: "They shall not grow old",
        filmPlot: "About filmedn;wj enkjebdfkdjbfkbebkebk ejbkbekbdkebdkeb jdkbjekbdjkejbdkejbdkjbkebjdke bjdkejbdkejbdkejbdkbjekjbdkbkebdjjedbkebdkebdkejbdejk",
        filmImage: project2,
        filmPath: "/single_film_page"
    },
    {
        filmName: "Journey's end",
        filmPlot: "About film",
        filmImage: project3,
        filmPath: "/single_film_page"
    },
    {
        filmName: "Light between oceans",
        filmPlot: "About film",
        filmImage: project4,
        filmPath: "/single_film_page"
    },
    {
        filmName: "Titanic",
        filmPlot: "About film",
        filmImage: "link",
        filmPath: "/single_film_page"
    },
    {
        filmName: "War Horse",
        filmPlot: "About film",
        filmImage: "link",
        filmPath: "/single_film_page"
    },
    {
        filmName: "Tolkien",
        filmPlot: "About film",
        filmImage: "link",
        filmPath: "/single_film_page"
    }
]


const Portfolio = () => {
    
    const classes = useStyles()

    return (
        <>
            <NavBar/>

            <Box component= "div" className={classes.mainContainer}>
            
                <Typography variant="h4" align="center" className= {classes.heading}>
                    Films for:
                </Typography>
                <Typography variant="h4" align="center" className= {classes.heading}>
                    Modern History - World War I
                </Typography>
                
                <Grid container justify="center">
                    
                    {filmList.map((lsItem) => (
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

export default Portfolio;