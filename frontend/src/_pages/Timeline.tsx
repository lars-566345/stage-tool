import React, { useState } from 'react';
import { Box, Typography, IconButton, SvgIcon } from '@mui/joy';
import SidebarStudent from '../_components/SidebarStudent';
import TimelinePhase from '../_components/TimelinePhase';
import DeliverableItem from '../_components/DeliverableItem';
import phaseData from '../_data/phaseData.json';

interface Deliverable {
  label: string;
}

interface Phase {
  title: string;
  description: string;
  deliverables: Deliverable[];
  identity?: string;
}

const Timeline: React.FC = () => {
  const [currentStartIndex, setCurrentStartIndex] = useState<number>(0);
  const [selectedDeliverables, setSelectedDeliverables] = useState<Record<number, number[]>>({});
  const [selectedPhaseIndex, setSelectedPhaseIndex] = useState<number>(0);

  const visiblePhasesCount = 3;
  const phases = phaseData as Phase[];
  const visiblePhases = phases.slice(currentStartIndex, currentStartIndex + visiblePhasesCount);

  const handlePrev = () => {
    setCurrentStartIndex((prev) => Math.max(prev - visiblePhasesCount, 0));
  };

  const handleNext = () => {
    setCurrentStartIndex((prev) =>
      Math.min(prev + visiblePhasesCount, phases.length - visiblePhasesCount)
    );
  };

  const toggleDeliverable = (index: number) => {
    setSelectedDeliverables((prev) => {
      const currentSelected = prev[selectedPhaseIndex] || [];
      const newSelected = currentSelected.includes(index)
        ? currentSelected.filter((i) => i !== index)
        : [...currentSelected, index];

      return {
        ...prev,
        [selectedPhaseIndex]: newSelected,
      };
    });
  };

  const currentPhase = phases[selectedPhaseIndex];

  return (
    <Box sx={{ display: 'flex' }}>
      <SidebarStudent />

      <Box sx={{ flex: 1, p: 4 }}>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
          <Typography level="h2" textAlign="center">
            Timeline
          </Typography>

          <Box
            sx={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 2,
              mb: { xs: 5, lg: 6 },
            }}
          >
            <IconButton
              onClick={handlePrev}
              disabled={currentStartIndex === 0}
              variant="outlined"
              size="lg"
            >
              <SvgIcon>
                <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z" />
              </SvgIcon>
            </IconButton>

            <Box
              sx={{
                display: 'flex',
                gap: 2,
                flexWrap: 'nowrap',
                overflowX: 'auto',
                width: '100%',
                justifyContent: 'center',
              }}
            >
              {visiblePhases.map((phase, index) => {
                const absoluteIndex = currentStartIndex + index;
                return (
                  <TimelinePhase
                    key={absoluteIndex}
                    label={phase.title}
                    active={absoluteIndex === selectedPhaseIndex}
                    onClick={() => setSelectedPhaseIndex(absoluteIndex)}
                  />
                );
              })}
            </Box>

            <IconButton
              onClick={handleNext}
              disabled={currentStartIndex + visiblePhasesCount >= phases.length}
              variant="outlined"
              size="lg"
            >
              <SvgIcon>
                <path d="M8.59 16.59L10 18l6-6-6-6-1.41 1.41L13.17 12z" />
              </SvgIcon>
            </IconButton>
          </Box>

          <Box>
            <Typography level="h4">Description</Typography>
            <Typography>{currentPhase.description}</Typography>
          </Box>

          <Box>
            <Typography level="h4">Deliverables</Typography>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
              {currentPhase.deliverables.map((item, index) => (
                <DeliverableItem
                  key={index}
                  label={item.label}
                  selected={(selectedDeliverables[selectedPhaseIndex] || []).includes(index)}
                  completed={true}
                  onClick={() => toggleDeliverable(index)}
                />
              ))}
            </Box>
          </Box>

          {currentPhase.identity && (
            <Box>
              <Typography level="h4">IT Identity</Typography>
              <Typography>{currentPhase.identity}</Typography>
            </Box>
          )}
        </Box>
      </Box>
    </Box>
  );
};

export default Timeline;
