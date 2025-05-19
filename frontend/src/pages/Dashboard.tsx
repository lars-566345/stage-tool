import Avatar from '@mui/joy/Avatar';
import Box from '@mui/joy/Box';
import Typography from '@mui/joy/Typography';
import Grid from '@mui/joy/Grid';
import Divider from '@mui/joy/Divider';
import Button from '@mui/joy/Button';



function Dashboard() {
  return (
    <>
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 2, // spacing between children
      }}>
        <Typography color="neutral" level="title-sm">Dashboard</Typography>
        <Avatar />
        <Typography level="h1">Lars de Wit</Typography>
        <Button
  color="danger"
  onClick={function(){}}
  size="lg"
  variant="outlined"> Test</Button>

        <Grid container spacing={2} sx={{ width: '100%' }}>
          <Grid xs={12} md={3}>
            <Box sx={{border: '1px solid', borderColor: 'divider', borderRadius: 'md',}}>
              <Box sx={{ bgcolor: 'primary.softBg', p: 2 }}>
                Evaluations
              </Box>
              <Divider />
              <Box sx={{ p: 2 }}>
                Content
              </Box>
            </Box>
          </Grid>
          <Grid xs={12} md={6}>
            <Box sx={{border: '1px solid', borderColor: 'divider', borderRadius: 'md',}}>
              <Box sx={{ bgcolor: 'primary.softBg', p: 2 }}>
                Timeline
              </Box>
              <Divider />
              <Box sx={{ p: 2 }}>
                Content
              </Box>
            </Box>
          </Grid>
          <Grid xs={12} md={3}>
            <Box sx={{border: '1px solid', borderColor: 'divider', borderRadius: 'md',}}>
                <Box sx={{ bgcolor: 'primary.softBg', p: 2 }}>
                  Semestercoaches
                </Box>
                <Divider />
                <Box sx={{ p: 2 }}>
                  Content
                </Box>
            </Box>
          </Grid>
          <Grid xs={12} md={6}>
            <Box sx={{border: '1px solid', borderColor: 'divider', borderRadius: 'md',}}>
                <Box sx={{ bgcolor: 'primary.softBg', p: 2 }}>
                  Pinned Posts
                </Box>
                <Divider />
                <Box sx={{ p: 2 }}>
                  Content
                </Box>
            </Box>
          </Grid>
          <Grid xs={12} md={6}>
            <Box sx={{border: '1px solid', borderColor: 'divider', borderRadius: 'md',}}>
                <Box sx={{ bgcolor: 'primary.softBg', p: 2 }}>
                  Pinned Posts
                </Box>
                <Divider />
                <Box sx={{ p: 2 }}>
                  Content
                </Box>
            </Box>
          </Grid>
        </Grid>
      </Box>

      
    </>
  );
}

export default Dashboard;