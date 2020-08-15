import React from 'react';
import NavBar from "../../components/NavBar";
import Header from "../../components/Header";
import Slider from "../../components/Slider";
import Particles from "react-particles-js";
import {makeStyles} from "@material-ui/styles";

const useStyles = makeStyles({
    particlesCanva: {
        position: "absolute",
        opacity: "0.3"
    },
    mainContainer: {
        height: "100%"
    },
    slider:{
        marginTop: "-20px"
    }
})

const Home = () => {

    const classes = useStyles()

    return(
        <>
            <div className={classes.mainContainer}>
                <>
                    <NavBar/>
                </>
                
            </div>
            <div className={classes.mainContainer}>
                <>
                    <Slider className={classes.slider} />
                </>
                
            </div>

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