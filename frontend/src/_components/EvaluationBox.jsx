import React, { useState } from 'react';
import { Box, Typography, Button, Textarea, Avatar } from '@mui/joy';

const EvaluationBox = ({ onSend }) => {
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (input.trim()) {
      onSend(input.trim());
      setInput('');
    }
  };

  return (
    <Box sx={{ backgroundColor: '#e0e0e0', p: 2, borderRadius: 2, mb: 2 }}>
      <Typography level="body-sm" mb={1}>Evaluation 4 &nbsp; | &nbsp; 10-04-2025</Typography>
      <Textarea
        placeholder="Type your evaluation here"
        minRows={4}
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <Box sx={{ textAlign: 'right', mt: 1 }}>
        <Button onClick={handleSend} variant="solid" sx={{backgroundColor:"#00838f"}}>Send</Button>
      </Box>
    </Box>
  );
};

export default EvaluationBox;