import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import Truncate from 'react-truncate';
import {
    Box,
    Grid,
    Card,
    CardActionArea,
    CardContent,
    CardMedia,
    Typography
} from "@material-ui/core";
import { Pagination } from  "@material-ui/lab";
import NavBar from "../../components/NavBar.js";
import axios from 'axios';
import { useState, useEffect } from 'react';
import { useParams } from "react-router";
import cat from "../../files/funny/cat.jpg";
import dog from "../../files/funny/dog.jpg";
import lama from "../../files/funny/lama.jpg";
import monkey from "../../files/funny/monkey.jpg";
import parrot from "../../files/funny/parrot.jpg";

const useStyles = makeStyles(theme => ({
    mainContainer: {
        background: "#AD5F3D",
        minHeight: "1080px",
    },
    heading: {
        color: "#FFB5A1",
        padding: "3rem 0 1.4rem",
        textTransform: "uppercase"
    },
    cardContainer: {
        maxWidth:300,
        margin: "2rem",
        color: "#B5A093"
    },
    overallCardRectangle: {
        height: "30rem",
        width: "19rem"
    },
    photoItem:{
        maxWidth: "10rem",
        height: "100%",
        marginTop: "1.3rem",
        marginBottom: "0.4rem"
    },
    errorMessage: {
        color: "#B5A093",
        margin: "2rem 5rem 2rem",
        [theme.breakpoints.up("md")]:{
            margin: "2rem 15rem 2rem"
        }
    },
    errorImageCard: {
        maxWidth: "35rem",
        maxHeight: "35rem"
    },
    photoError: {
        height: "100%",
        width: "100%"
    },
    pagination: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        paddingBottom: "2rem",
        '& > *': {
          marginTop: theme.spacing(2),
        },
      }
}))

const photoArr = [
    cat,
    dog,
    lama,
    monkey,
    parrot
]

function random_item(items){
    return items[Math.floor(Math.random() * items.length)]
}

const FilmsList = () => {
    
    const randomPhoto = random_item(photoArr);

    const [filmList, setFilmList] = useState([]);
    const [pagesCount, setPagesCount ] = useState(0);

    const [PeriodSubperiodDict, setPeriodSubperiodDict] = useState({});

    const [pageNumber, setPageNumber] = useState(1);

    const handleChange = (event, value) => {
        setPageNumber(value);
        axios.get(`http://127.0.0.1:5000/films_list/${subperiod_id}?page_number=${value}`).then((films) => setFilmList(films.data.films_list));
    };

    const { subperiod_id } = useParams();

    useEffect(() => {
        axios.get(`http://127.0.0.1:5000/films_list/${subperiod_id}?page_number=${pageNumber}`).then((films) => {
            setFilmList(films.data.films_list);

            const { total_films_number, films_per_page } = films.data;
            let numberOfPages = Math.trunc(total_films_number / films_per_page);
            if ( (numberOfPages % films_per_page) !== 0 ) {numberOfPages++}
            setPagesCount(numberOfPages);
        });
        axios.get(`http://127.0.0.1:5000/subperiod_period_names/${subperiod_id}`).then((period_subperiod) => setPeriodSubperiodDict(period_subperiod.data));

    },[]);

    const classes = useStyles()

    return (
        <>
            <NavBar/>

            <Box component= "div" className={classes.mainContainer}>
                <div className= {classes.heading}>
                    <Typography variant="h4" align="center" >
                        Films for:
                    </Typography>

                    <Typography variant="h4" align="center">
                        {PeriodSubperiodDict["period_name"]} - {PeriodSubperiodDict["subperiod_name"]}
                    </Typography>

                </div>
                <Grid container justify="center">
                    {filmList.length === 0 && (   
                        <>

                            <Typography variant="h6" align="center" className ={classes.errorMessage}>
                                We are sorry but there are no current film matching your current request.
                            </Typography>
                        
                            <Card className= {classes.errorImageCard}>
                                <CardMedia 
                                    component="img" 
                                    image={randomPhoto}
                                    className={classes.photoError}
                                />
                            </Card>

                        </>
                    )}
                    {filmList.map((lsItem) => (
                        <Grid item xs={12} sm={8} md={6} className={classes.cardContainer} >
                            <Card align="center" className= {classes.overallCardRectangle}>
                                <CardActionArea href={`/selected_film/${subperiod_id}/${lsItem["film_id"]}`} >

                                    <CardMedia 
                                        className= {classes.photoItem}
                                        component="img" 
                                        image={lsItem["film_image_url"]}
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5">
                                            {lsItem["film_name"]}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            <Truncate lines={4} ellipsis={"..."}>
                                                {lsItem["film_plot"]}
                                            </Truncate>
                                        </Typography>
                                    </CardContent>
                                </CardActionArea>
                            </Card>

                        </Grid>
                    ))}


                </Grid>
                { pagesCount !== 0 &&
                    <div className= {classes.pagination}>
                        <Pagination count={pagesCount} page={pageNumber} onChange={handleChange} showFirstButton showLastButton />
                    </div>
                }
            </Box>
        </>
        )
}

export default FilmsList;

