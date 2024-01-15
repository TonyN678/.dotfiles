---@diagnostic disable: trailing-space
return {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
      config = function()
        require("lualine").setup({
         
         options = {
            theme = "dracula"
                },
        
         sections = {
             lualine_x = {
        
                {
                'fileformat',
                 symbols = {
                 unix = '', --  e712
                 dos = '',  --  e70f
                 mac = '',  --  e711
                            }
                },

                {

                },

                        }

                  },
        })
    end
}
