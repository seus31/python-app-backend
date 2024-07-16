import React from 'react'
import { LocalizationProvider } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import './App.css'
import { ApolloClient, ApolloProvider, HttpLink, InMemoryCache } from '@apollo/client'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { getAccessToken, getStatus } from './libs/auth'
import { setContext } from '@apollo/client/link/context'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import LoginContainer from './components/containers/LoginContainer'

const authLink = setContext((_, { headers }) => {
  const token = getAccessToken()
  const status = getStatus()
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : '',
      "X-STATUS": status,
    },
  }
})

const client = new ApolloClient({
  link: authLink.concat(
      new HttpLink({
        uri: 'http://localhost:3000/graphql',
      })
  ),
  cache: new InMemoryCache(),
})

const mdTheme = createTheme({
  palette: {
    //primary: { main: '#0bbe78' }
  }
})

const App: React.FC = () => {
  return (
      <ThemeProvider theme={mdTheme}>
        <BrowserRouter>
          <ApolloProvider client={client}>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <Routes>
                <Route path="/login" Component={LoginContainer} />
              </Routes>
            </LocalizationProvider>
          </ApolloProvider>
        </BrowserRouter>
      </ThemeProvider>
  )
}

export default App