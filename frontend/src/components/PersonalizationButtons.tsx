import React from 'react';

interface PersonalizationButtonsProps {
  onPersonalize: () => void;
  onTranslateUrdu: () => void;
}

const PersonalizationButtons: React.FC<PersonalizationButtonsProps> = ({
  onPersonalize,
  onTranslateUrdu,
}) => {
  return (
    <div style={{ margin: '10px 0', display: 'flex', gap: '10px' }}>
      <button onClick={onPersonalize} style={{ padding: '8px 12px', cursor: 'pointer' }}>
        Personalize Content
      </button>
      <button onClick={onTranslateUrdu} style={{ padding: '8px 12px', cursor: 'pointer' }}>
        اردو ترجمہ (Urdu Translation)
      </button>
    </div>
  );
};

export default PersonalizationButtons;
