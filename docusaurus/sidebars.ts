import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'ROS 2',
      items: ['ros2/chapter1', 'ros2/chapter2', 'ros2/chapter3'],
    },
    {
      type: 'category',
      label: 'Gazebo/Unity',
      items: ['gazebo-unity/chapter1', 'gazebo-unity/chapter2', 'gazebo-unity/chapter3'],
    },
    {
      type: 'category',
      label: 'NVIDIA Isaac',
      items: ['nvidia-isaac/chapter1', 'nvidia-isaac/chapter2', 'nvidia-isaac/chapter3'],
    },
    {
      type: 'category',
      label: 'VLA',
      items: ['vla/chapter1', 'vla/chapter2', 'vla/chapter3'],
    },
  ],
};

export default sidebars;
