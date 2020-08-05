import React from 'react';
import NavBar from "../../components/NavBar.js";
import Header from "../../components/Header.js";
import Particles from "react-particles-js";
import {makeStyles} from "@material-ui/styles";

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
            }}
            />

        </>

        )
};

export default Home;