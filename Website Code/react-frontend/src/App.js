import React, { useState, useEffect } from 'react';
import { Route } from 'react-router-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import './App.css';

import SelectedFilm from './pages/single_film_page/selected_film.js';
// import Timeline from './pages/timeline_page/timeline_selection.js';
import Home from './pages/home/home.js';
import PeriodTimeline from './pages/period_timeline_page/period_timeline';
import SubperiodTimeline from './pages/subperiod_timeline_page/subperiod_timeline';
import FilmsList from './pages/films_list_page/films_list.js';
import Portfolio from './pages/portfolio/portfolio.js';

export default function App() {
  
  return (
    <>
      <CssBaseline/>
      <Route exact path="/" component={Home}/>
      <Route path="/period_timeline" component={PeriodTimeline}/>
      <Route path="/subperiod_timeline" component={SubperiodTimeline}/>
      <Route path="/films_list" component={FilmsList}/>
      <Route path="/single_film_page" component={SelectedFilm}/>
      <Route path="/portfolio" component={Portfolio}/>
    </>
  );
}