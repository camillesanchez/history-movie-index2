import React from 'react';
import NavBar from "../../components/NavBar";
import Header from "../../components/Header";
import Slider from "../../components/Slider";
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

const Home = () => {

    const classes = useStyles()

    return(
        <>
            <NavBar/>
            
            <Slider/>
        </>

        )
};

export default Home;

// { <Particles 
//     canvasClassName = {classes.particlesCanva}
//     params = {{
//         particles:{
//             number:{
//                 value: 90,
//                 density: {
//                     enable: true,
//                     value_area: 900
//                 }
//             },
//             shape: {
//                 type: "circle",
//                 stroke:{
//                     width: 0.5,
//                     color: "tomato"
//                 } 
//             },
//             size: {
//                 value: 3,
//                 random: true,
//                 anim: {
//                     enable: true,
//                     speed: 6,
//                     size_min: 0.1,
//                     sync: true
//                 }
//             },
//             opacity: {
//                 value: 1,
//                 random: true,
//                 anim:{
//                     enable: true,
//                     speed: 1,
//                     opacity_min: 0.1,
//                     sync: true
//                 }
//             }
//         }
//     }}/> }