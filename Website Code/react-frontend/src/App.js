import React, { useState, useEffect } from 'react';
import { Route } from 'react-router-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import './App.css';

import SelectedFilm from './pages/single_film_page/selected_film.js';
import Home from './pages/home/home';
import About from './pages/about_page/about'
import PeriodTimeline from './pages/period_timeline_page/period_timeline';
import SubperiodTimeline from './pages/subperiod_timeline_page/subperiod_timeline';
import FilmsList from './pages/films_list_page/films_list';

export default function App() {
  
  return (
    <>
      <CssBaseline/>
      <Route exact path="/" component={Home}/>
      <Route exact path="/about" component={About}/>
      <Route path="/period_timeline" component={PeriodTimeline}/>
      <Route path="/subperiod_timeline/:period_id" component={SubperiodTimeline}/>
      <Route path="/films_list/:subperiod_id" component={FilmsList}/>
      <Route path="/selected_film/:subperiod_id/:film_id" component={SelectedFilm}/>
    </>
  );
}