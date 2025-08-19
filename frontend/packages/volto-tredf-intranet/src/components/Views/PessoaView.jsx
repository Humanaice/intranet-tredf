import React from 'react';
import { Container } from '@plone/components';
import UniversalLink from '@plone/volto/components/manage/UniversalLink/UniversalLink';
import Image from '@plone/volto/components/theme/Image/Image';
import ContactInfo from '../ContactInfo/ContactInfo';
import EnderecoInfo from '../EnderecoInfo/EnderecoInfo';

const PessoaView = (props) => {
  const { content } = props;
  return (
    <Container narrow id="page-document" className="view-wrapper pessoa-view">
      {content.image && (
        <Container className={'image'}>
          <Image
            className="documentImage ui right floated image"
            alt={content.title}
            title={content.title}
            item={content}
            imageField="image"
            responsive={true}
          />
        </Container>
      )}
      {content.cargo && (
        <span className={`cargo cargo-${content.cargo.token}`}>
          {content.cargo.title}
        </span>
      )}
      <h1 className="documentFirstHeading">{content.title}</h1>
      {content.area && (
        <UniversalLink className={'area'} item={content.area}>
          {content.area.title}
        </UniversalLink>
      )}
      {content.description && (
        <p className="documentDescription">{content.description}</p>
      )}
      <EnderecoInfo content={content} />
      <ContactInfo content={content} />
    </Container>
  );
};

export default PessoaView;
