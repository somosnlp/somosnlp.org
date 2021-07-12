<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script><template>
    <nav class="flex gap-4 items-center justify-between select-none">
        <div class="flex gap-8 items-center">
            <Logo />
            <router-link
                to="/blog"
                class="whitespace-nowrap hover:text-accent-500"
            >{{ t('navbar.blog') }}</router-link>
            <router-link
                to="/about"
                class="whitespace-nowrap hover:text-accent-500"
            >{{ t('navbar.about') }}</router-link>
        </div>
        <div class="flex gap-4 items-center">
            <div class="flex gap-2" text="lg">
                <SocialMediaButtons />
            </div>
            <DarkThemeToggle />
        </div>
    </nav>
</template>
