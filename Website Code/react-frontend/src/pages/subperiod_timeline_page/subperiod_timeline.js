import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import { Typography, Box, List, ListItem} from "@material-ui/core";
import { Link } from "react-router-dom";
import NavBar from "../../components/NavBar.js";

// CSS Styles
const useStyles = makeStyles(theme => ({
    mainContainer: {
        background: "#AD5F3D"
    },
    timeLine: {
        position: "relative",
        padding: "1rem",
        margin: "0 auto",
        "&:before": {
            content: "''",
            position: "absolute",
            height: "100%",
            border: "1px solid tan",
            right: "40px",
            top: 0
        },
        "&:after": {
            content: "''",
            display: "table",
            clear: "both"
        },
        [theme.breakpoints.up("md")]:{
            padding: "2rem",
            "&:before": {
                left: "calc(50% - 1px)",
                right: "auto"
            }
        }
    },
    timeLineItem: {
        padding: "1rem",
        borderBottom: "2px solid tan",
        position: "relative",
        margin: "1rem 3rem 1rem 1rem",
        clear: "both",
        "&:after":{
            content:"''",
            position: "absolute"
        },
        "&:before": {
            content: "''",
            position: "absolute",
            right: "-0.625rem",
            top: "calc(50% -5px)",
            borderStyle: "solid",
            borderColor: "tomato tomato transparent transparent",
            borderWidth: "0.625rem",
            transform: "rotate(45deg)"
        },
        [theme.breakpoints.up("md")]:{
            width: "44%",
            margin: "1rem",
            "&:nth-of-type(2n)": {
                float:"right",
                margin: "1rem",
                borderColor: "tan"
            },
            "&:nth-of-type(2n):before": {
                right: "auto",
                left: "-0.625rem",
                borderColor: "transparent transparent tomato tomato"
            }
        }
    },
    timeLineYear: {
        textAlign: "center",
        maxWidth: "9.375rem",
        margin: "0 3rem 0 auto",
        fontSize: "1.8rem",
        background: "blue",
        color: "white",
        lineHeight: 1,
        padding: "0.5rem 0 1rem",
        "&:before":{
            display: "none"
        },
        [theme.breakpoints.up("md")]:{
            textAlign: "center",
            margin: "0 auto",
            "&:nth-of-type(2n)": {
                float:"none",
                margin: "0 auto"
            },
            "&:nth-of-type(2n):before": {
                display: "none"
            }
        }
    },
    heading: {
        color: "tomato",
        padding: "3rem 0",
        textTransform: "uppercase"
    },
    subHeading: {
        color: "white",
        padding: "0",
        textTransform: "uppercase"
    }
}));

const subperiodItems = [
  {
    itemStartDate: "3600 BCE",
    itemPeriod: "Bronze Age",
    itemDates: "Dates: 3600 BCE - 600 BCE",
    itemLocations: "All",
    itemPath: "/portfolio"
  },
  {
    itemStartDate: "3500 BCE",
    itemPeriod: "Old Kingdom",
    itemDates: "Dates: 3500 BCE - 2050 BCE",
    itemLocations: "Egypt",
    itemPath: "/portfolio"
  },
  {
    itemStartDate: "2600 CE",
    itemPeriod: "Indus Vakkey Civilisation",
    itemDates: "Dates: 2600 BCE - 1800 BCE",
    itemLocations: "India",
    itemPath: "/portfolio"
  },
  {
    itemStartDate: "2000 BCE",
    itemPeriod: "Middle Kingdom",
    itemDates: "Dates: 2000 BCE - 1650 BCE",
    itemLocations: "Egypt",
    itemPath: "/portfolio"
  },
  {
    itemStartDate: "1700 BCE",
    itemPeriod: "Shang Dynasty",
    itemDates: "Dates: 1700 BCE - 1200 BCE",
    itemLocations: "China",
    itemPath: "/portfolio"
  }
]

// NEED TO FIX THE VISUAL BECAUSE OF LINE ITEM!! Would be great if goes back to one side vs the other
const SubperiodTimeline = () => {
    
    const classes = useStyles()

    return (
        <>
            <NavBar />
            <Box component="header" className={classes.mainContainer}> 
                <Typography variant="h4" align="center" className= {classes.heading}> 
                    Subperiod Timeline
                </Typography>
                <Box component="div" className={classes.timeLine}> 
                    <List>
                        {subperiodItems.map((lsItem, key) => (
                            <ListItem button key={key} component={Link} to={lsItem.itemPath}>
                            
                                <Typography variant="h2" className={`${classes.timeLineYear} ${classes.timeLineItem}`}>
                                    {lsItem.itemStartDate}
                                </Typography>
                                <Box component= "div" className={classes.timeLineItem}>
                                    <Typography variant="h5" align= "center" className={classes.subHeading}>
                                        {lsItem.itemPeriod}
                                    </Typography>
                                    <Typography variant="body1" align= "center" style={{color: "tomato"}}>
                                        {lsItem.itemDates}
                                    </Typography>
                                    <Typography variant="subtitle1" align= "center" style={{color: "tan"}}>
                                        {lsItem.itemLocations}
                                    </Typography>
                                </Box>
                            </ListItem>
                        ))}
                    </List>
                </Box>
                
            </Box>

        </>


        )
};


export default SubperiodTimeline;

