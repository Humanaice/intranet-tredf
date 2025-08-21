import React from 'react';
import { Container } from '@plone/components';
import Icon from '@plone/volto/components/theme/Icon/Icon';
import userSVG from '@plone/volto/icons/user.svg';

const PessoaGridItem = ({ item }) => {
  return (
    <div className={`card-inner`}>
      <div className={`card-summary`}>
        <Container className="areaInfo">
          <Icon name={userSVG} size="64px" className={'icon listitem'} />
          <h2 className="title">{item.title}</h2>
          <p className="description">{item.description}</p>
        </Container>
      </div>
    </div>
  );
};

export default PessoaGridItem;
