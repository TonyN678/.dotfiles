---@diagnostic disable: trailing-space
return {
  
  -- mason is a lsp or language server protocol manager
  -- or more simpler: programming language's syntax helper
  {
    "williamboman/mason.nvim",
    config = function()
      require("mason").setup()
    end
  },
  
  -- This tool connects mason and lspconfig from nvim together to make it easier to configure
  -- Instead of the old way to connect them manually
  {
    "williamboman/mason-lspconfig.nvim",
    config = function()
      require("mason-lspconfig").setup({
          ensure_installed = {"lua_ls", "pyright",}
      })
    end
  },
  
  -- This is the original lsp in nvim come by default
  {
    "neovim/nvim-lspconfig",
    config = function()
      
      local capabilities = require('cmp_nvim_lsp').default_capabilities()

      local lspconfig = require('lspconfig')
      local lsp_servers = {"lua_ls", "pyright", "bashls", "cssls", "html",}  
      
      for _, server in ipairs(lsp_servers) do
        lspconfig[server].setup({capabilities=capabilities})
      end
      --lspconfig.pylsp.setup({capabilities=capabilities})
      --lspconfig.lua_ls.setup({capabilities=capabilities})

      vim.keymap.set('n', 'gd', vim.lsp.buf.definition, {})
      vim.keymap.set({ 'n', 'v' }, '<leader>ca', vim.lsp.buf.code_action, {})
      vim.keymap.set('n', 'K', vim.lsp.buf.hover, {})
    end
  },

}
