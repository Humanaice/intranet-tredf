import React from 'react';
import UniversalLink from '@plone/volto/components/manage/UniversalLink/UniversalLink';
import { Container } from '@plone/components';

const AreaInfo = ({ content }) => {
  const { area } = content;

  return (
    <Container narrow className="area-info">
      <h1>Área</h1>
      <UniversalLink className={'area'} item={area}>
        <h2>{area.title}</h2>
      </UniversalLink>
      <p>{area.description}</p>
    </Container>
  );
};

export default AreaInfo;
