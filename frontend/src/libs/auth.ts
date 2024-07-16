export const setAccessToken = (token: string) => {
    return localStorage.setItem('token', token)
}

export const getAccessToken = () => {
    return localStorage.getItem('token')
}

export const removeAccessToken = () => {
    return localStorage.removeItem('token')
}

export const getStatus = () => {
    return localStorage.getItem('status')
}

export const setStatus = (status: string) => {
    return localStorage.setItem('status', status)
}

export const removeStatus = () => {
    return localStorage.removeItem('status')
}