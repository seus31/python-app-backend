import * as React from 'react'
import { Title } from '@mui/icons-material'
import { Container, Grid, Typography } from '@mui/material'
import Layout from '../common/Layout'
import StyledPaper from '../common/styled/StyledPaper'

type DashboardProps = {}

const Dashboard = (props: DashboardProps) => {
  return (
    <Layout>
      <Container maxWidth="xl" sx={{ mt: 4, mb: 4 }}>
        <StyledPaper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
          <Grid container spacing={2} p={2}>
            <Grid item xs={12} p={2}>
              <Typography variant="h4">ダッシュボード</Typography>
            </Grid>
          </Grid>
        </StyledPaper>
      </Container>
      <Container maxWidth="xl" sx={{ mt: 4, mb: 4 }}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <StyledPaper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
              <React.Fragment>
                <Title>ダッシュボード</Title>
              </React.Fragment>
            </StyledPaper>
          </Grid>
        </Grid>
      </Container>
    </Layout>
  )
}

export default Dashboard
