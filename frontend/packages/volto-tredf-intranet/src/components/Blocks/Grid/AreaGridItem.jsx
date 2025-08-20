import React from 'react';
import AreaInfo from '../../AreaInfo/AreaInfo';

const AreaGridItem = ({ item }) => {
  return (
    <div className={`card-inner`}>
      <div className={`card-summary`}>
        <AreaInfo content={item} icon />
      </div>
    </div>
  );
};

export default AreaGridItem;
