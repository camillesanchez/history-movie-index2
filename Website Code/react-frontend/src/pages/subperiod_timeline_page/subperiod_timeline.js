import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import { Typography, Box, List, ListItem} from "@material-ui/core";
import { Link } from "react-router-dom";
import NavBar from "../../components/NavBar.js";
import axios from 'axios';
import { useState, useEffect } from 'react';
import { useParams } from "react-router";

// CSS Styles
const useStyles = makeStyles(theme => ({
    mainContainer: {
        background: "#AD5F3D",
        minHeight: "1080px"
    },
    timeLine: {
        position: "relative",
        padding: "1rem",
        margin: "0 auto",
        "&:before": {
            content: "''",
            position: "absolute",
            height: "100%",
            border: "1px solid #B5A093",
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
        borderBottom: "2px solid #B5A093",
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
            borderColor: "#FFB5A1 #FFB5A1 transparent transparent",
            borderWidth: "0.625rem",
            transform: "rotate(45deg)"
        },
        [theme.breakpoints.up("md")]:{
            width: "44%",
            margin: "1rem",
            "&:nth-of-type(2n)": {
                float:"right",
                margin: "1rem",
                borderColor: "#B5A093"
            },
            "&:nth-of-type(2n):before": {
                right: "auto",
                left: "-0.625rem",
                borderColor: "transparent transparent #FFB5A1 #FFB5A1"
            }
        }
    },
    timeLineYear: {
        textAlign: "center",
        maxWidth: "9.375rem",
        margin: "0 3rem 0 auto",
        fontSize: "1.8rem",
        background: "#B58D82",
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
        color: "#FFB5A1",
        padding: "3rem 0",
        textTransform: "uppercase"
    },
    subHeading: {
        color: "white",
        padding: "0",
        textTransform: "uppercase"
    }
}));

const SubperiodTimeline = () => {
    
    const [filmList, setFilmList] = useState([]);

    const { period_id } = useParams();

    useEffect(() => {
        axios.get(`http://127.0.0.1:5000/subperiod_timeline/${period_id}`).then((films) => setFilmList(films.data));
    },[]);

    const classes = useStyles()

    return (
        <>
            <NavBar />
            <Box component="header" className={classes.mainContainer}> 
                <Typography variant="h4" align="center" className= {classes.heading}> 
                    Subperiod Timeline
                </Typography>

                <Box component="div" className={classes.timeLine}> 
                    {filmList.map((lsItem) => (
                        <Link style={{ textDecoration: 'none' }} to={`/films_list/${lsItem["subperiod_id"]}`}>
                            <Typography variant="h2" className={`${classes.timeLineYear} ${classes.timeLineItem}`}>
                                {lsItem["subperiod_start_date"]}
                            </Typography>
                            <Box component= "div" className={classes.timeLineItem}>
                                <Typography variant="h5" align= "center" className={classes.subHeading}>
                                    {lsItem["subperiod_name"]}
                                </Typography>
                                <Typography variant="body1" align= "center" style={{color: "#FFB5A1"}}>
                                    {lsItem["subperiod_dates"]}
                                </Typography>
                                <Typography variant="subtitle1" align= "center" style={{color: "#B58D82"}}>
                                    {lsItem["subperiods_locations"]}
                                </Typography>

                            </Box>
                        </Link>
                    ))}
                </Box>
                
            </Box>

        </>


        )
};

export default SubperiodTimeline;

