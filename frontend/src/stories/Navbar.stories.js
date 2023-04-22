// Button.stories.js

import NavbarComponent  from './../components/NavbarComponent.vue';

export default {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/vue/configure/overview#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: 'NavbarComponent',
  component: NavbarComponent,
};

/*
 *👇 Render functions are a framework specific feature to allow you control on how the component renders.
 * See https://storybook.js.org/docs/vue/api/csf
 * to learn how to use render functions.
 */
export const Primary = {
  render: () => ({
    components: { NavbarComponent },
    template: `
    <NavbarComponent >dsadsadas</NavbarComponent>`,
  }),
};
