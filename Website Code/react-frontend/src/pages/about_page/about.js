import React from 'react';
import NavBar from "../../components/NavBar.js";
import { makeStyles } from "@material-ui/core/styles";
import {
    Box,
    Grid,
    Card,
    CardMedia,
    Typography
} from "@material-ui/core";
import world from '../../files/world.jpg'

const useStyles = makeStyles({
    mainContainer: {
        background: "#AD5F3D",
        height: "100%"
    },
    heading: {
        color: "#FFB5A1",
        padding: "3rem 0 3rem",
        textTransform: "uppercase"
    },
    text: {
        color:"#B5A093",
        padding: "0rem 3rem 1.4rem",
    },
    textHeading: {
        color:"#B5A093",
        padding: "0rem 3rem 0rem",
        textDecorationLine: "underline"
    },
    highlightedWords: {
        color:"#F5E7DF",
    },
    photo: {
        height: "100%",
        width: "100%"
    },
    imageCard: {
        maxWidth: "35rem",
        maxHeight: "35rem",
        marginBottom: "3rem"
    }
})
export default function About() {

    const classes = useStyles()

  return (
    <>
        <NavBar/>
        <Box component= "div" className={classes.mainContainer}>
            <>
                <Typography variant= "h4" align="center" className={classes.heading}>
                    About
                </Typography>
                    
                <Typography variant= "h6" align="center" className={classes.text}>
                    The 21st century is considered as the <b>Digital Era</b>, but our education system is still mainly based on textbook-learning, despite children, teenagers, and young adults watching hours of films.
                </Typography>
                <Typography variant= "h6" align="center" className={classes.textHeading}>
                    <b>Our Goal: </b>
                </Typography>
                <Typography variant= "h6" align="center" className={classes.text}>
                    Providing a place for teachers, students and parents to <b>find films by time periods</b> they want to watch to discover the period visually.
                </Typography>
            </>
            <Grid container justify="center">
                <Card className= {classes.imageCard}>
                    <CardMedia 
                        component="img" 
                        image= {world}
                        className={classes.photo}
                        align = "center"
                    />
                </Card>
            </Grid>
        </Box>
      
    </>

)};
