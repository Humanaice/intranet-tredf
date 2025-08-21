import { cloneDeep } from 'lodash';

import AreaView from './components/Views/AreaView';
import PessoaView from './components/Views/PessoaView';
// Blocos
import AreaGridItem from './components/Blocks/Grid/AreaGridItem';
import PessoaGridItem from './components/Blocks/Grid/PessoaGridItem';
/// Clima
import ClimaEdit from './components/Blocks/Clima/Edit';
import ClimaView from './components/Blocks/Clima/View';
import climaSVG from '@plone/volto/icons/cloud.svg';

const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['pt-br'];
  config.settings.defaultLanguage = 'pt-br';
  config.settings.image_crop_aspect_ratios = [
    {
      label: '16:9',
      ratio: 16 / 9,
    },
    {
      label: '4:3',
      ratio: 4 / 3,
    },
    {
      label: '1:1',
      ratio: 1,
    },
  ];
  // Registra Visoes padrao para tipos de conteúdo
  config.views.contentTypesViews = {
    Area: AreaView,
    Pessoa: PessoaView,
    ...config.views.contentTypesViews,
  };

  // Blocos
  /// Grid
  config.registerComponent({
    name: 'GridListingItemTemplate',
    component: AreaGridItem,
    dependencies: 'Area',
  });
  config.registerComponent({
    name: 'GridListingItemTemplate',
    component: PessoaGridItem,
    dependencies: 'Pessoa',
  });
  /// Clima
  config.blocks.blocksConfig.climaBlock = {
    id: 'climaBlock',
    title: 'Clima',
    group: 'common',
    icon: climaSVG,
    view: ClimaView,
    edit: ClimaEdit,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
    blockHasOwnFocusManagement: false,
  };

  // Adiciona blocos ao Grid
  const localBlocks = ['climaBlock'];

  // Add Blocks to gridBlock
  // It's important to maintain the chain, and do not introduce pass by reference in
  // the internal `blocksConfig` object, so we clone the object to avoid this.
  ['gridBlock'].forEach((blockId) => {
    const block = config.blocks.blocksConfig[blockId];
    if (
      block !== undefined &&
      block.allowedBlocks !== undefined &&
      block.blocksConfig !== undefined
    ) {
      block.allowedBlocks = [...block.allowedBlocks, ...localBlocks];
      localBlocks.forEach((blockId) => {
        block.blocksConfig[blockId] = cloneDeep(
          config.blocks.blocksConfig[blockId],
        );
      });
    }
  });

  return config;
};

export default applyConfig;
