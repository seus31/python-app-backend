import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import App from './App'
import reportWebVitals from './reportWebVitals'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@fontsource/roboto/300.css'
import '@fontsource/roboto/400.css'
import '@fontsource/roboto/500.css'
import '@fontsource/roboto/700.css'

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
)

const token = localStorage.getItem('token')
if (token === null || token === undefined) {
    if (window.location.pathname !== '/login') {
        window.location.href = '/login'
    }
}

root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
)

reportWebVitals()