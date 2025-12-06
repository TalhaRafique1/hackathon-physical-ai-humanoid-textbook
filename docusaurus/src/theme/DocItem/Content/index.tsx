import React from 'react';
import DocItemContent from '@theme-original/DocItem/Content';
import PersonalizationButtons from '../../../../../frontend/src/components/PersonalizationButtons'; // Adjusted path

export default function DocItemContentWrapper(props): JSX.Element {
  // Placeholder functions for button actions
  const handlePersonalize = () => {
    console.log('Personalize Content clicked!');
    // Implement personalization logic here
  };

  const handleTranslateUrdu = () => {
    console.log('Urdu Translation clicked!');
    // Implement Urdu translation logic here
  };

  return (
    <>
      <DocItemContent {...props} />
      <PersonalizationButtons
        onPersonalize={handlePersonalize}
        onTranslateUrdu={handleTranslateUrdu}
      />
    </>
  );
}
