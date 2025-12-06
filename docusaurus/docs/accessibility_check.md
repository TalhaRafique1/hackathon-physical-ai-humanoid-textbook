# Website Accessibility Check (WCAG)

To ensure the Docusaurus site is compliant with WCAG (Web Content Accessibility Guidelines), perform the following checks:

1.  **Automated Tools**: Use accessibility checkers like Axe DevTools (browser extension) or Lighthouse (built into Chrome DevTools) to scan your site.
2.  **Manual Review**:
    *   **Keyboard Navigation**: Ensure all interactive elements are reachable and usable via keyboard.
    *   **Semantic HTML**: Verify correct use of headings, lists, and ARIA attributes where necessary.
    *   **Color Contrast**: Check text and background color contrast for readability.
    *   **Focus Management**: Ensure focus indicators are visible.
    *   **Screen Reader Compatibility**: Test key user flows with a screen reader (e.g., NVDA, JAWS, VoiceOver).
3.  **Content Accessibility**:
    *   **Image Alt Text**: All meaningful images should have descriptive `alt` text.
    *   **Link Text**: Link text should be descriptive and make sense out of context.
    *   **Headings**: Use headings correctly to convey document structure.

**Tools to use**:
-   [Axe DevTools](https://www.deque.com/axe/devtools/)
-   [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
-   [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
