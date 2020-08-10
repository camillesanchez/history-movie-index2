import React from 'react';
import NavBar from "../../components/NavBar.js";
import Header from "../../components/Header.js";
import Particles from "react-particles-js";
import {makeStyles} from "@material-ui/styles";
import axios from 'axios';
import { useState } from 'react';
import colisee from "../../files/covers/colisee.jpg";
import gladiator from "../../files/covers/Gladiator-Movie.jpg";
import black_women from "../../files/covers/black-women-equal-rights.jpg";
import hidden_figures from "../../files/covers/Hidden-Figures-Movie.jpg";
import shipwreck from "../../files/covers/Titanic-wreck.jpg";
import titanic from "../../files/covers/titanic-movie-cover.jpg";

const useStyles = makeStyles({
    particlesCanva: {
        position: "absolute",
        opacity: "0.3"
    }
})

const imageItems = [
    {
        imageLink: colisee,
        imageDesc: "Colisee image"
    },
    {
        imageLink: gladiator,
        imageDesc: "Gladiator movie cover"
    },
    {
        imageLink: black_women,
        imageDesc: "Black women marching for equal rights" 
    },
    {
        imageLink: hidden_figures,
        imageDesc: "Hidden Figures movie cover"
    },
    {
        imageLink: shipwreck,
        imageDesc: "Titanic underwater wreck"
    },
    {
        imageLink: titanic,
        imageDesc: "Titanic movie cover"
    }
];

const Home = () => {
    
    const [filmList, setFilmList] = useState([]);

    const response = axios.get("http://127.0.0.1:5000/").then((films) => setFilmList(films.data))
    // to get an item: {filmList}

    const classes = useStyles()

    return(
        <>
            <NavBar/>
            <Header/>
            <Particles 
            canvasClassName = {classes.particlesCanva}
            params = {{
                particles:{
                    number:{
                        value: 90,
                        density: {
                            enable: true,
                            value_area: 900
                        }
                    },
                    shape: {
                        type: "circle",
                        stroke:{
                            width: 0.5,
                            color: "tomato"
                        } 
                    },
                    size: {
                        value: 3,
                        random: true,
                        anim: {
                            enable: true,
                            speed: 6,
                            size_min: 0.1,
                            sync: true
                        }
                    },
                    opacity: {
                        value: 1,
                        random: true,
                        anim:{
                            enable: true,
                            speed: 1,
                            opacity_min: 0.1,
                            sync: true
                        }
                    }
                }
            }}/>

        </>

        )
};

export default Home;