import React, { useState } from 'react';
import {  makeStyles } from '@material-ui/core';
import "./slider.scss";
import ImgComp from "./ImgComp";
import Header from "./Header";
import colisee from "../files/covers/colisee.jpg";
import gladiator from "../files/covers/Gladiator-Movie.jpg";
import black_women from "../files/covers/black-women-equal-rights.jpg";
import hidden_figures from "../files/covers/Hidden-Figures-Movie.jpg";
import shipwreck from "../files/covers/Titanic-wreck.jpg";
import titanic from "../files/covers/titanic-movie-cover.jpg";
import worldwar1cover from "../files/covers/1917cover.jpg";
import worldwar1 from "../files/covers/worldwar1.jpg";


function Slider(){

    const useStyles = makeStyles(theme=>({
        buttonText:{
            fontSize: "20px",
            color: "#B58D82",
            outline: "black"
        }
    }))

    let sliderArr = [
        <ImgComp src={colisee}/>,
        <ImgComp src={gladiator}/>,
        <ImgComp src={black_women}/>,
        <ImgComp src={hidden_figures}/>,
        <ImgComp src={worldwar1}/>,
        <ImgComp src={worldwar1cover}/>,       
        <ImgComp src={shipwreck}/>,
        <ImgComp src={titanic}/>,
    ]

    const [x, setX] = useState(0);

    const classes = useStyles()

    const goLeft = () => {

        x === 0 ? setX(-100 * (sliderArr.length-1)) : setX(x + 100);
    };
    const goRight = () => {
        (x === - 100 * (sliderArr.length-1)) ? setX(0) : setX(x - 100);
    };

    return (
            
        <>
            <Header/>
            <div className="slider">
                {sliderArr.map((item, index) => {
                    return (
                        <div key={index} className="slide" style={{transform: `translateX(${x}%)`}}  >
                            {item}
                        </div>
                    );
                })}
                <button id ="goLeft" onClick={goLeft} className={classes.buttonText}> <b>Left</b></button>
                <button id ="goRight" onClick={goRight} className={classes.buttonText}> <b>Right</b></button>
            </div>
        </>

    )
}

export default Slider;