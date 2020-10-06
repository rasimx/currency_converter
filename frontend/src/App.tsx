import React, {useState, useEffect, SyntheticEvent, BaseSyntheticEvent} from 'react';

import './App.css';

import 'whatwg-fetch'

import Api from "./components/Api";

import {createStyles, makeStyles, Theme} from '@material-ui/core/styles';
import {
  Toolbar,
  AppBar,
  Typography,
  Paper,
  Container,
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
  TextField,
  Box, Button
} from "@material-ui/core";
import DoubleArrow from '@material-ui/icons/DoubleArrow';
import Grid from '@material-ui/core/Grid';
import ICurrencyRate from "./config/ICurrencyRate";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      flexGrow: 1,
    },
    title: {
      flexGrow: 1,
    },
    paper: {
      padding: theme.spacing(2),
      textAlign: 'center',
      color: theme.palette.text.secondary,
    },
    main: {
      paddingTop: '20px'
    },
    table: {
      width: '100%',
    },
  }),
);

let initValue = 1

function App() {
  const classes = useStyles();
  const [currencyRates, setCurrencyRates] = useState<ICurrencyRate[]>([])
  const [currentCurrency, setCurrentCurrency] = useState<ICurrencyRate | null>()
  const [currentValue, setCurrentValue] = useState<string>('0')


  useEffect(() => {
    Api.getCurrencies().then((rates: ICurrencyRate[]) => {
      setCurrencyRates(rates)
      let currentCurrency = rates[0]
      setCurrentCurrency(currentCurrency)
      if (currentCurrency) setCurrentValue((parseFloat(currentCurrency.value)*initValue).toString())
    }).catch(err => {
      alert('Error fetch currencies')
    })
  }, []);

  function onInput(ev: BaseSyntheticEvent) {
    initValue = ev.target.value
    if (currentCurrency && initValue) {
      Api.getRate('USD', currentCurrency.target.code, initValue.toString()).then((rate) => {
        setCurrentValue(rate.result)
      })
    }
  }

  function btnOnClick(currencyRate: ICurrencyRate): void {
    setCurrentCurrency(currencyRate);
    console.log(initValue)
    Api.getRate('USD', currencyRate.target.code, initValue.toString()).then((rate) => {
      setCurrentValue(rate.result)
    })
  }

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Container>
          <Toolbar>
            <Typography variant="h6" className={classes.title}>
              Currency converter
            </Typography>
          </Toolbar>
        </Container>
      </AppBar>
      <main className={classes.main}>
        <Container>
          <Grid container spacing={3}>
            <Grid item xs={4}>
              <TableContainer component={Paper}>
                <Table className={classes.table} aria-label="simple table">
                  <TableHead>
                    <TableRow>
                      <TableCell>Currency</TableCell>
                      <TableCell align="right">Rate</TableCell>
                      <TableCell align="right"></TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {currencyRates.map((currencyRate: ICurrencyRate) => (
                      <TableRow key={currencyRate.target.code}>
                        <TableCell component="th" scope="row">
                          {currencyRate.target.code}
                        </TableCell>
                        <TableCell align="right">{currencyRate.value}</TableCell>
                        <TableCell align="right">
                          <Button variant="contained"
                                  onClick={() => btnOnClick(currencyRate)}
                                  color={currentCurrency && currencyRate.target.code == currentCurrency.target.code ? "primary" : "default"}>Choise</Button>
                        </TableCell>

                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </Grid>
            <Grid item xs={8}>
              <Paper className={classes.paper}>
                Base currency - USD {currentCurrency && `, Target - ${currentCurrency.target.code}`}
              </Paper>
              <Paper className={classes.paper}>
                <Box display="flex" alignItems="center" justifyContent="center">
                  <TextField type="number" variant="outlined" onChange={onInput} defaultValue={initValue}/>
                  <DoubleArrow/>
                  <TextField type="number" variant="outlined" disabled={true} value={currentValue}/>
                </Box>
              </Paper>
            </Grid>
          </Grid>
        </Container>
      </main>
    </div>
  );
}

export default App;
