---@diagnostic disable: trailing-space
return {
    'goolord/alpha-nvim',
    config = function ()
        --require'alpha'.setup(require'alpha.themes.dashboard'.config)
        local alpha = require'alpha'
         local dashboard = require'alpha.themes.dashboard'
        -- Set header
        dashboard.section.header.val = {
      -- "                                                     ",
      -- "                                                     ",
      -- "  ███╗   ██╗███████╗ ██████╗ ██╗   ██╗██╗███╗   ███╗ ",
      -- "  ████╗  ██║██╔════╝██╔═══██╗██║   ██║██║████╗ ████║ ",
      -- "  ██╔██╗ ██║█████╗  ██║   ██║██║   ██║██║██╔████╔██║ ",
      -- "  ██║╚██╗██║██╔══╝  ██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║ ",
      -- "  ██║ ╚████║███████╗╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║ ",
      -- "  ╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝ ",
      -- "                                                     ",
      -- "           󰈸  It should be totally okay  󰈸           ",
      -- "                                                     ",
      -- "                                                     ",
      -- "                                                     ",
      -- "                                                     ",
    

	[[                                                                       ]],
	[[                                                                       ]],
	[[  ██████   █████                   █████   █████  ███                  ]],
	[[ ░░██████ ░░███                   ░░███   ░░███  ░░░                   ]],
	[[  ░███░███ ░███   ██████   ██████  ░███    ░███  ████  █████████████   ]],
	[[  ░███░░███░███  ███░░███ ███░░███ ░███    ░███ ░░███ ░░███░░███░░███  ]],
	[[  ░███ ░░██████ ░███████ ░███ ░███ ░░███   ███   ░███  ░███ ░███ ░███  ]],
	[[  ░███  ░░█████ ░███░░░  ░███ ░███  ░░░█████░    ░███  ░███ ░███ ░███  ]],
	[[  █████  ░░█████░░██████ ░░██████     ░░███      █████ █████░███ █████ ]],
	[[ ░░░░░    ░░░░░  ░░░░░░   ░░░░░░       ░░░      ░░░░░ ░░░░░ ░░░ ░░░░░  ]],
	[[                                                                       ]],
	[[                                                                       ]],
  [[                󰈸  The codes in still running fine  󰈸                  ]], 
	[[                                                                       ]],
	[[                                                                       ]],
    }

        -- Set menu
        dashboard.section.buttons.val = {
        dashboard.button("e", "  > New file", ":ene <BAR> startinsert <CR>"),
        dashboard.button("f", "󱝩  > Find file", ":Telescope find_files hidden=true no_ignore=true<CR>"),
        dashboard.button("r", "  > Recent files", "<cmd>Telescope oldfiles<CR>"),
        dashboard.button("l", "󰁯  > Open last session", "<cmd>RestoreSession<CR>"),
        dashboard.button("c", "  > Configuration", ":e ~/.config/nvim/init.lua <CR>"),
        dashboard.button("u", "  > Update plugins", ":Lazy sync<CR>"),
        dashboard.button("q", "  > Quit", ":qa<CR>")
        }

        dashboard.section.footer.val = {
            "                                                                                        ",
            "                                                                                        ",
            "      \"Intelligence is the ability to avoid doing work, yet getting the work done.\"      ",
            "                                                                                         ",
            "                                      - Linus Torvalds                                     ",               
      
            }

         alpha.setup(dashboard.config)
    end
}
