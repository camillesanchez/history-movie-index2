import React from 'react';
import Typed from "react-typed";
import {makeStyles} from "@material-ui/core/styles";

import {
    Typography,
    Avatar,
    Grid,
    Box
} from '@material-ui/core';
import avatar from '../files/avatar.png';

// CSS Styles
const useStyles = makeStyles(theme=>({
  avatar:{
    width:theme.spacing(10),
    height:theme.spacing(10),
    margin:theme.spacing(1),
  },
  title:{
    color: "#AD5F3D"
  },
  subtitle:{
    color: "#B5A093",
    marginBottom: "3rem"
  },
  typedContainer: {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: "100vw",
    textAlign: "center",
    zInder: 1
  }
}));

const Header = () => {
    const classes = useStyles()
  return (
    <Box className={classes.typedContainer} >
        <Grid container justify ="center">
            <Avatar className={classes.avatar} src= {avatar} alt="Camille" />
        </Grid>
        <Typography className={classes.title} variant="h4">
            <Typed strings={["History Movie Index"]} typeSpeed={40}/>
        </Typography>
        <br/>
        <Typography className={classes.subtitle} variant="h6">
            <Typed strings={["By Camille Sanchez", "NYU SPS Capstone Project"]} typeSpeed={40} backSpeed= {60} loop/>
        </Typography>
    </Box>
    );
};

export default Header;