import React from 'react'
import { LocalizationProvider } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import './App.css'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import { ApiProvider } from './providers/ApiContext'
import { AuthProvider, useAuth } from './providers/AuthContext'
import DashboardContainer from './components/containers/DashboardContainer'
import LoginContainer from './components/containers/LoginContainer'
import RegisterContainer from './components/containers/RegisterContainer'

const mdTheme = createTheme({
  palette: {
    //primary: { main: '#0bbe78' }
  }
})

const apiUrl = 'http://localhost:5555/api/v1'

const App: React.FC = () => {
  return (
    <ThemeProvider theme={mdTheme}>
      <BrowserRouter>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <AuthProvider>
            <ApiProvider apiUrl={apiUrl}>
              <Routes>
                <Route path="/login" Component={LoginContainer} />
                <Route path="/register" Component={RegisterContainer} />
                <Route path="/dashboard" Component={DashboardContainer} />
                <Route path="*" element={<Navigate to="/login" />} />
              </Routes>
            </ApiProvider>
          </AuthProvider>
        </LocalizationProvider>
      </BrowserRouter>
    </ThemeProvider>
  )
}

export default App
