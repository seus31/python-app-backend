import React from 'react'
import LoginForm from '../presenters/LoginForm'
import { useMutation, useQuery } from '@apollo/client'
import { useNavigate } from 'react-router-dom'
import { Box, LinearProgress } from '@mui/material'
import {removeAccessToken, removeStatus, setAccessToken, setStatus} from '../../libs/auth'
//import { LoggedInAdministratorDocument, SignInMutationDocument } from '../../generated/graphql'

const LoginContainer = () => {
    const navigate = useNavigate()
    // const [signIn] = useMutation(SignInMutationDocument)
    // const { loading, data } = useQuery(LoggedInAdministratorDocument, { variables: { token: localStorage.getItem('token') } })
    //
    // if (loading) {
    //     return (
    //         <Box sx={{ width: '100%' }}>
    //             <LinearProgress />
    //         </Box>
    //     )
    // } else if (data?.loggedAdministrator.token) {
    //     window.location.href = '/'
    // } else {
    //     removeStatus()
    //     removeAccessToken()
    // }
    //
    // const handleLoginSuccess = async (credentialResponse: CredentialResponse) => {
    //     const { data } = await signIn({ variables: { input: { code: credentialResponse.credential } }})
    //
    //     if (data.signIn.token !== null) {
    //         setAccessToken(data.signIn.token)
    //         setStatus('loggedIn')
    //         navigate('/')
    //     } else {
    //         alert(data.signIn.errors[0])
    //     }
    // }
    //
    // const handleLoginError = async () => {
    //     console.log('login failed!')
    // }

    return (
        <LoginForm />
    )
}

export default LoginContainer