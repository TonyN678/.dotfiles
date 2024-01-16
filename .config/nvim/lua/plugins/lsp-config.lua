return {
  {
    "williamboman/mason.nvim",
    config = function()
      require("mason").setup()
    end
  },

  {
    "williamboman/mason-lspconfig.nvim",
    config = function()
      require("mason-lspconfig").setup({
          ensure_installed = {"lua_ls", "pylsp"}
      })
    end
  },

  {
    "neovim/nvim-lspconfig",
    config = function()
      local lspconfig = require('lspconfig')
      lspconfig.pylsp.setup({})
      lspconfig.lua_ls.setup({})

      vim.keymap.set('n', 'gd', vim.lsp.buf.definition, {})
      vim.keymap.set({ 'n', 'v' }, '<leader>ca', vim.lsp.buf.code_action, {})
      vim.keymap.set('n', 'K', vim.lsp.buf.hover, {})
    end
  },

}