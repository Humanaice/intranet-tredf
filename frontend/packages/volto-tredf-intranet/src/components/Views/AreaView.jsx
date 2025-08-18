import React from 'react';
import { getBaseUrl } from '@plone/volto/helpers';
import { Container } from '@plone/components';
import ContactInfo from '../ContactInfo/ContactInfo';
import EndereçoInfo from '../EnderecoInfo/EnderecoInfo';
import RenderBlocks from '@plone/volto/components/theme/View/RenderBlocks';

const AreaView = (props) => {
  const { content, location } = props;
  const path = getBaseUrl(location?.pathname || '');

  return (
    <Container id="page-document" className="view-wrapper area-view">
      <RenderBlocks {...props} path={path} />
      <ContactInfo content={content} />
      <EndereçoInfo content={content} />
    </Container>
  );
};

export default AreaView;
