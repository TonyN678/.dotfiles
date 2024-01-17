---@diagnostic disable: trailing-space
return {
  
  -- These plugins are for the nvim-cmp to communicate with the language server
  -- in order to get syntax suggestions and completion
  {
    'hrsh7th/cmp-nvim-lsp',
    dependencies = {
      'hrsh7th/cmp-buffer',
      'hrsh7th/cmp-cmdline',
      'hrsh7th/cmp-path',
    }
  },

  -- plugins for provide suggestions
  {
    'L3MON4D3/LuaSnip',
      dependencies = {
    'saadparwaiz1/cmp_luasnip', 'rafamadriz/friendly-snippets'}
  },
  
  -- A program manage the snippet window and allow interaction by cmp_luasnip
  {
  "hrsh7th/nvim-cmp",
  config = function()
    local cmp = require'cmp'
    require("luasnip.loaders.from_vscode").lazy_load()
  cmp.setup({
    snippet = {
      -- REQUIRED - you must specify a snippet engine
      expand = function(args)
         require('luasnip').lsp_expand(args.body) -- For `luasnip` users.
        -- require('snippy').expand_snippet(args.body) -- For `snippy` users.
        -- vim.fn["UltiSnips#Anon"](args.body) -- For `ultisnips` users.
      end,
    },
    window = {
          -- Allow completion interaction and documentation when hovered
       completion = cmp.config.window.bordered(),
       documentation = cmp.config.window.bordered(),
    },
        -- Keys for interacting with suggested snippets
    mapping = cmp.mapping.preset.insert({
      ['<C-b>'] = cmp.mapping.scroll_docs(-4),
      ['<C-f>'] = cmp.mapping.scroll_docs(4),
      ['<C-Space>'] = cmp.mapping.complete(),
      ['<C-e>'] = cmp.mapping.abort(),
      ['<CR>'] = cmp.mapping.confirm({ select = true }), -- Accept currently selected item. Set `select` to `false` to only confirm explicitly selected items.
    }),
    sources = cmp.config.sources({
      { name = 'nvim_lsp' },
       { name = 'luasnip' }, -- For luasnip users.
      -- { name = 'ultisnips' }, -- For ultisnips users.
      -- { name = 'snippy' }, -- For snippy users.
    }, {
      { name = 'buffer' },
    })
  })
  end

  }
}
