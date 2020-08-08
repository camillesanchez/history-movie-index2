import React, {useState} from 'react';
import MobilRightMenuSlider from '@material-ui/core/Drawer';
import { Link } from "react-router-dom";
import {
  ArrowBack,
  Timeline,
  Home,
  Movie,
  ContactMail,
  ContactSupport,
  MenuIcon
} from '@material-ui/icons';
import {
  AppBar,
  Toolbar,
  IconButton,
  Button,
  Typography,
  ListItem,
  ListItemText,
  ListItemIcon,
  Avatar,
  Divider,
  List,
  Box,
  makeStyles
  } from '@material-ui/core';
import avatar from '../files/avatar.png';

// CSS Styles
const useStyles = makeStyles(theme=>({
  menuSliderContainer:{
    width: 250,
    background: "#B5A093",
    height: "100%"
  },
  avatar:{
    display: "block",
    margin: "0.5rem auto",
    width:theme.spacing(13),
    height:theme.spacing(13)
  },
  listItem:{
    color: "white"
  }
}));

const menuItems = [
  {
    listIcon: <Home/>,
    listText: "Home",
    listPath: "/"
  },
  {
    listIcon: <Timeline/>,
    listText: "Timeline",
    listPath: "/period_timeline"
  },
  {
    listIcon: <Movie/>,
    listText: "Selected Movie"
  },
  {
    listIcon: <ContactSupport/>,
    listText: "Comments/ Feddbacks"
  }
]


const NavBar = () => {

  const [state, setState] = useState({
    right: false
  })

  const toggleSlider = (slider,open) => () => {
    setState({...state, [slider]: open})
  }
  const classes = useStyles()

  const sideList = slider => (
    <Box 
    className={classes.menuSliderContainer} 
    component="div"
    onClick={toggleSlider(slider, false)}
    >
      <Avatar className={classes.avatar} src={avatar} alt="Camille"/>
      <Divider/>
        <List>
          {menuItems.map((lsItem, key) => (
            <ListItem button key={key} component={Link} to={lsItem.listPath}>
              <ListItemIcon className={classes.listItem}> {lsItem.listIcon} </ListItemIcon>
              <ListItemText className={classes.listItem} primary={lsItem.listText}/>
            </ListItem>
          ))}
        </List>
      </Box>
    )
  return (
    <>

      <Box component= "nav">
        <AppBar position= "static" style={{background: "#B58D82"}}>
          <Toolbar>
            <IconButton onClick={toggleSlider("right", true)}>
              <ArrowBack style={{color: "white"}}/>
            </IconButton>
            <Typography variant = "h6" style={{color: "white"}}>History Movie Index</Typography>
            <MobilRightMenuSlider anchor="right" open={state.right} onClose={toggleSlider("right", false)} >
              {sideList("right")}
            </MobilRightMenuSlider>
          </Toolbar>
        </AppBar>
      </Box>
    </>

  )
};

export default NavBar;